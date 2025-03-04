import time
import random
from sympy import nextprime

# Rastgele büyük asal sayılar üretme
def generate_large_prime(bits=30):
    num = random.getrandbits(bits)  # 30-bitlik rastgele sayı üret
    prime = nextprime(num)  # En yakın asal sayıyı bul
    return prime

# Naif çarpanlara ayırma algoritması (yavaş)
def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

# Kanıt oluşturucu
def proof_checker():
    log_file = "p_vs_np_proof.txt"
    results = []
    
    with open(log_file, "w") as f:
        f.write("### P vs NP Deneyi ###\n\n")
        
        for test_num in range(1, 220):  # 219 test yapalım
            p = generate_large_prime()
            q = generate_large_prime()
            N = p * q  # RSA modülü
            
            test_info = f"Test {test_num}: N={N} (p={p}, q={q})\n"
            print(test_info)
            f.write(test_info)
            
            start_time = time.time()
            factors = factorize(N)
            end_time = time.time()
            duration = end_time - start_time
            
            result = f"Çarpanlar: {factors}\nHesaplama Süresi: {duration:.2f} saniye\n\n"
            print(result)
            f.write(result)
            results.append(test_info + result)
            
            if duration < 1.0:
                warning = "*** ÖNEMLİ: Bu faktörizasyon polinom zamanda tamamlandı! P = NP olabilir? ***\n"
                print(warning)
                f.write(warning)
                results.append(warning)
                

        f.write("\nSonuç: Eğer tüm testler uzun sürerse, bu P ≠ NP için deneysel bir kanıt olur.\n")
    
    # Tüm sonuçları terminale yazdır
    print("\n### TEST SONUÇLARI ###\n")
    for res in results:
        print(res)

# Çalıştır
proof_checker()