from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import json
from typing import Optional, Dict
from typing import Dict
import re
from base64 import b64decode, b64encode

# (¡DEBE COINCIDIR CON LA DE POSTMAN!)
# clave de 32 bytes (256 bits)

CLAVE_SECRETA_STR = "Clave16BytesAES!"
CLAVE_SECRETA_BYTES = CLAVE_SECRETA_STR.encode('utf-8')

def decrypt_packet_aes(paquete_cifrado: Dict) -> Optional[Dict]:
    """
    Descifra un diccionario de datos cifrados AES-CBC recibidos del cliente.

    Args:
        paquete_cifrado: Diccionario con 'iv' y 'payload' (ambos en Base64).

    Returns:
        Diccionario (JSON) con los datos descifrados en texto plano, o None si falla.
    """
    
    # Validar la estructura del paquete
    if 'iv' not in paquete_cifrado or 'payload' not in paquete_cifrado:
        print("Error: Paquete cifrado incompleto (falta IV o payload)")
        return None

    try:
        # Decodificar Base64
        iv = b64decode(paquete_cifrado['iv'])
        datos_cifrados = b64decode(paquete_cifrado['payload'])

        # Validar longitud del IV
        if len(iv) != 16:
             raise ValueError("IV tiene longitud incorrecta.")

        # Configurar el Descifrador AES-CBC
        cipher = Cipher(
            algorithms.AES(CLAVE_SECRETA_BYTES), 
            modes.CBC(iv), 
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        
        #  Descifrar los datos
        # Esto incluye el padding que debe ser removido (finalize lo hace)
        datos_descifrados_con_padding = decryptor.update(datos_cifrados) + decryptor.finalize()
        
        # Decodificar a string (texto plano)
        datos_plano_str = datos_descifrados_con_padding.decode('utf-8').strip()

        # 
        # Regex para encontrar el primer carácter '{' y el último carácter '}'
        # y toma SOLO el contenido entre ellos. Esto ignora cualquier basura fuera de ellos     
        
        # Patrón que busca el inicio de un JSON ({) y el final (})
        match = re.search(r'\{.*\}', datos_plano_str, re.DOTALL)
        
        if match:
            datos_limpios = match.group(0)
        else:
            # Si no encuentra el JSON válido, falla.
            raise ValueError("No se pudo extraer el JSON válido de los datos descifrados.")
        
        print(datos_limpios)
        #  Convertir la string JSON a un diccionario de Python
        return json.loads(datos_limpios)
        
    except ValueError as ve:
        # Maneja errores de padding incorrecto, longitud de clave/IV, etc.
        print(f"Error criptográfico/validación: {ve}")
        return None
    except Exception as e:
        # Maneja errores de decodificación JSON, etc.
        print(f"Error general en el descifrado: {e}")
        return None
    

def crypt_packet_aes(datos_plano: Dict) -> Dict:
    """
    Cifra un diccionario de Python (datos en texto plano) usando AES-256-CBC.

    Genera un IV único para cada cifrado y devuelve el paquete listo para enviar 
    al cliente (Postman).
    
    Args:
        datos_plano: Diccionario de Python con los datos a cifrar.

    Returns:
        Diccionario con 'iv' y 'payload' (ambos en Base64).
    """
    
    # 1. Convertir el diccionario de Python a una cadena JSON (texto plano)
    datos_plano_json = json.dumps(datos_plano, ensure_ascii=False)
    datos_plano_bytes = datos_plano_json.encode('utf-8')

    # 2. Generar un Vector de Inicialización (IV) aleatorio y único (16 bytes)
    iv = os.urandom(16)
    
    # 3. Configurar el Cifrador AES-CBC
    cipher = Cipher(
        algorithms.AES(CLAVE_SECRETA_BYTES), 
        modes.CBC(iv), 
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # 4. Cifrar los datos
    # La librería maneja automáticamente el padding (PKCS7) necesario.
    datos_cifrados = encryptor.update(datos_plano_bytes) + encryptor.finalize()
    
    # 5. Codificar el IV y el Payload a Base64 (para ser seguros en JSON)
    paquete_cifrado = {
        'iv': b64encode(iv).decode('utf-8'),
        'payload': b64encode(datos_cifrados).decode('utf-8')
    }
    
    return paquete_cifrado
