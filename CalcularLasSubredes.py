def convertir_a_binario(ip):
    #Convierte una IP en formato decimal a una cadena binaria.
    octetos = ip.split('.')
    binario = ''.join(bin(int(octeto))[2:].zfill(8) for octeto in octetos)
    return binario

def convertir_a_decimal(binario):
    #Convierte una IP en formato binario a una cadena en formato decimal.
    octetos = [binario[i:i+8] for i in range(0, 32, 8)]
    decimal = '.'.join(str(int(octeto, 2)) for octeto in octetos)
    return decimal

def calcular_and(ip_binario, mascara_binario):
    #Realiza la operación AND entre la IP y la máscara en formato binario.
    resultado = ''.join('1' if ip_binario[i] == '1' and mascara_binario[i] == '1' else '0' for i in range(32))
    return resultado

def calcular_or(ip_binario, complemento_mascara_binario):
    #Realiza la operación OR entre la IP y el complemento de la máscara en formato binario.
    resultado = ''.join('1' if ip_binario[i] == '1' or complemento_mascara_binario[i] == '1' else '0' for i in range(32))
    return resultado

def calcular_complemento_mascara(mascara_binario):
    #Calcula el complemento de la máscara en formato binario.
    complemento = ''.join('0' if bit == '1' else '1' for bit in mascara_binario)
    return complemento

def main():
    # Ingresamos la red completa con la IP y la máscara
    ip_red_y_mascara = input("Ingresar la ip con su mascara(192.168.10.10/24): ")

    # Dividimos para obtener la IP y la máscara
    ip_red, mascara = ip_red_y_mascara.split('/')
    mascara = int(mascara)

    # Convertimos la IP a binario
    ip_binario = convertir_a_binario(ip_red)

    # Creamos la máscara en binario
    mascara_binario = '1' * mascara + '0' * (32 - mascara)

    # Calculamos la dirección de red usando AND
    ip_red_binario = calcular_and(ip_binario, mascara_binario)
    ip_red_decimal = convertir_a_decimal(ip_red_binario)

    # Calculamos el complemento de la máscara
    complemento_mascara_binario = calcular_complemento_mascara(mascara_binario)

    # Calculamos la dirección de broadcast usando OR
    ip_broadcast_binario = calcular_or(ip_binario, complemento_mascara_binario)
    ip_broadcast_decimal = convertir_a_decimal(ip_broadcast_binario)

    # Calculamos el número de hosts
    num_hosts = (2**(32 - mascara)) - 2
    num_subredes = (2**(32 - mascara))

    # Imprimimos la información
    print('Dirección de red:', ip_red_decimal)
    print('Dirección de broadcast:', ip_broadcast_decimal)
    print('Número de subredes:', num_subredes)
    print('Número de hosts:', num_hosts)

if __name__ == "__main__":
    main()