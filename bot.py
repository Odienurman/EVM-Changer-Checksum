from web3 import Web3

# Menampilkan banner
banner = "=" * 50
header = "Join our Telegram: https://t.me/sigundulmania"
print(banner)
print(header)
print(banner)

addresses = [
    "your_EVM_address",
    "your_EVM_address"
]

checksum_addresses = [Web3.to_checksum_address(address) for address in addresses]

# Menyimpan hasil ke file address.txt
with open("address.txt", "w") as file:
    file.write(banner + "\n")
    file.write(header + "\n")
    file.write(banner + "\n")
    for addr in checksum_addresses:
        file.write(addr + "\n")
        print(addr)
