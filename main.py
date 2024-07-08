def char_to_binary(char):
    """
    将字符转换为二进制字符串
    """
    return format(ord(char), '016b')  # 使用16位二进制表示字符的Unicode码

def binary_to_root_node(binary_str):
    """
    将二进制字符串转换为root和node组成的字符串
    """
    return binary_str.replace('0', 'root').replace('1', 'node')

def root_node_to_binary(root_node_str):
    """
    将root和node组成的字符串转换回二进制字符串
    """
    return root_node_str.replace('root', '0').replace('node', '1')

def encrypt(text):
    """
    加密函数，将输入文本转换为由root和node组成的字符串
    """
    encrypted_text = ""
    for char in text:
        binary_str = char_to_binary(char)
        encrypted_char = binary_to_root_node(binary_str)
        encrypted_text += encrypted_char + " "
    return encrypted_text.strip()

def decrypt(encrypted_text):
    """
    解密函数，将由root和node组成的字符串还原为原文本
    """
    decrypted_text = ""
    encrypted_chars = encrypted_text.split(' ')
    for encrypted_char in encrypted_chars:
        binary_str = root_node_to_binary(encrypted_char)
        char = chr(int(binary_str, 2))
        decrypted_text += char
    return decrypted_text

# 测试代码
if __name__ == "__main__":
    original_text = "牛逼"
    encrypted_text = encrypt(original_text)
    decrypted_text = decrypt(encrypted_text)
    
    print("原始文本:", original_text)
    print("加密文本:", encrypted_text)
    print("解密文本:", decrypted_text)
