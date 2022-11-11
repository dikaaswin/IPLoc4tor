# Import modul2

import geocoder, fontstyle, pyfiglet, termcolor

from pyfiglet import figlet_format

from termcolor import colored

from colored import fg

# Headers

print((colored(figlet_format("IP Loc4tor", font = "jazmine"), "cyan")))

# Copyright

print(fontstyle.apply("[ ✔ ] Creator : 7Security", "bold/italic/yellow"))

# Pilihan

print(fontstyle.apply("""

        ------------------------

        |     Pilihan          |

        ------------------------

        | A | Lacak IP sendiri |

        ------------------------

        | B | Lacak IP lain    |

        ------------------------

        [!] Penulisan memakai huruf besar

        Misalnya A / B""", "bold/bold/cyan"))

# Suruh memilih

tanyakan = input(fontstyle.apply("Pilih : ", "bold/bold/yellow"))

ip_address_1 = geocoder.ip("me")

color = fg("green")

# Print IP sendiri

if tanyakan == "A":

        print(color + f"[✔] Alamat         : ", ip_address_1.address)

        print(f"[✔] Kota           : ", ip_address_1.city)

        print(f"[✔] Negara         : ", ip_address_1.country)

        print(f"[✔] Alamat IP      : ", ip_address_1.ip)

        print(f"[✔] Latitude       : ", ip_address_1.lat)

        print(f"[✔] Longitude      : ", ip_address_1.lng)

        print(f"[✔] Ok             : ", ip_address_1.ok)

        print(f"[✔] Organisasi/ISP : ", ip_address_1.org)

        print(f"[✔] Provinsi       : ", ip_address_1.state)

        print(f"[✔] Status         : ", ip_address_1.status)

        print(f"[✔] Nama Host      : ", ip_address_1.hostname)

        print(f"[✔] Kode ZIP       : ", ip_address_1.postal)

color_1 = fg("green")

# Tanyakan IP

if tanyakan == "B":

        tanya = input(fontstyle.apply("[!] Masukkan Alamat IP : ", "bold/bold/yellow"))

        ip_address = geocoder.ip(tanya)

        print(color_1 + f"[✔] Alamat         : ", ip_address.address)

        print(f"[✔] Kota           : ", ip_address.city)

        print(f"[✔] Negara         : ", ip_address.country)

        print(f"[✔] Alamat IP      : ", ip_address.ip)

        print(f"[✔] Latitude       : ", ip_address.lat)

        print(f"[✔] Longitude      : ", ip_address.lng)

        print(f"[✔] Ok             : ", ip_address.ok)

        print(f"[✔] Organisasi/ISP : ", ip_address.org)

        print(f"[✔] Provinsi       : ", ip_address.state)

        print(f"[✔] Status         : ", ip_address.status)

        print(f"[✔] Nama Host      : ", ip_address.hostname)

        print(f"[✔] Kode ZIP       : ", ip_address.postal)
