import geocoder, fontstyle

print(fontstyle.apply("""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

| o  .oPYo.   o                      .8    o                |

| 8  8    8   8                     d'8    8                |

| 8 o8YooP'   8     .oPYo. .oPYo.  d' 8   o8P .oPYo. oPYo.  |

| 8  8        8     8    8 8    ' Pooooo   8  8    8 8  `'  |

| 8  8        8     8    8 8    .     8    8  8    8 8      |

| 8  8        8oooo `YooP' `YooP'     8    8  `YooP' 8      |

| ..:..:::::::......:.....::.....:::::..:::..::.....:..:::: |

| ::::::::::::::::::::::::::::::::::::::::::::::::::::::::: |

| ::::::::::::::::::::::::::::::::::::::::::::::::::::::::: |

|                                                           |

| Author: 7Security                                         |

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|

""", "bold/bold/yellow"))

print(fontstyle.apply("""

        -------------------------

        |     Choice            |

        -------------------------

        | A | Track Your Own IP |

        -------------------------

        | B | Track Another IP  |

        -------------------------

        [!] Write in capital letters!

        For example A or B""", "bold/bold/green"))

print("\n")

ask = input(fontstyle.apply("Choose : ", "bold/bold/yellow"))

ip_address_1 = geocoder.ip("me")

if ask == "A":

        print(fontstyle.apply(f"[✔] Address        : {ip_address_1.address}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] City           : {ip_address_1.city}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Country        : {ip_address_1.country}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] IP             : {ip_address_1.ip}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Latitude       : {ip_address_1.lat}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] Longitude      : {ip_address_1.lng}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Ok             : {ip_address_1.ok}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] Org/ISP        : {ip_address_1.org}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Province       : {ip_address_1.state}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] Status         : {ip_address_1.status}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Host Name      : {ip_address_1.hostname}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] ZIP Code       : {ip_address_1.postal}", "bold/bold"))

if ask == "B":

        ask_1 = input(fontstyle.apply("[!] Enter IP : ", "bold/bold/yellow"))

        ip_address = geocoder.ip(ask_1)

        print(fontstyle.apply(f"[✔] Address        : {ip_address.address}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] City           : {ip_address.city}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Country        : {ip_address.country}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] IP             : {ip_address.ip}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Latitude       : {ip_address.lat}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] Longitude      : {ip_address.lng}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Ok             : {ip_address.ok}", "bold/bold/grcyan"))

        print(fontstyle.apply(f"[✔] Org/ISP        : {ip_address.org}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Province       : {ip_address.state}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] Status         : {ip_address.status}", "bold/bold"))

        print(fontstyle.apply(f"[✔] Host Name      : {ip_address.hostname}", "bold/bold/cyan"))

        print(fontstyle.apply(f"[✔] ZIP Code       : {ip_address.postal}", "bold/bold"))
