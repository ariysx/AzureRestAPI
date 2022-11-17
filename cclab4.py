import requests
import json


def main():
    vm_url = "https://management.azure.com/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/lab4vm?api-version=2022-08-01"
    ni_url = "https://management.azure.com/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/test-ni?api-version=2022-05-01"
    ip_url = "https://management.azure.com/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/test-ip?api-version=2022-05-01"

    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2Njg2OTA4OTQsIm5iZiI6MTY2ODY5MDg5NCwiZXhwIjoxNjY4Njk2MjQzLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBeVZDSzNGb1J5bk41R25HelRRUVlyc3dXcWx1Ym8zZGYvNitUVjNHUnBleWtmcm5TbFNFK1BjcW9tdVRoa1B3QjBGRDdQZzlVUUt5bkRnbklBOEk4K2dUN09TNHNQLzVkVmY2SDFIdnVTUFk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTGFrc2FuYWtlc2ltIiwiZ2l2ZW5fbmFtZSI6IkNoYWtrYXJpbiIsImdyb3VwcyI6WyI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCIxMjVjYWI3Yy1mOWViLTQzZTUtOWUyMS01ZTNiNWRkZDA1YmEiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiXSwiaXBhZGRyIjoiMTQ3LjI1Mi4yMy4yMTYiLCJuYW1lIjoiRDIxMTI1Mzg3IENoYWtrYXJpbiBMYWtzYW5ha2VzaW0iLCJvaWQiOiIzMTU2NDhhMy02MzdmLTQ3YmItOTFkNi03YjE2YTIwYzljZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMzk3NDUiLCJwdWlkIjoiMTAwMzIwMDE3MzQxNDMyRSIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBRUEuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiSTNWQ3BGSk50UmhJTHFuemJWZ2FvT0N1X3VkcGdXNHdJTjNqSGV5VzVKTSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiRDIxMTI1Mzg3QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJEMjExMjUzODdAbXl0dWR1Ymxpbi5pZSIsInV0aSI6IkpRWmZwQUhuV2ttSGhjZWFMemtSQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.aMjh4zFkJtIqDgMZit0aC6-1vWtQJiiU40Ie0z7pyCWqnB3q7gBOUR3r1X9rROuNaRdif_97-jaBQGs7AOpTFqdmvhTQG24ksfdXB7RdCMx6E52oQ0tBhZLZyXhWZBhuTU4vyPufqYleCf26yIo45gKmczQvPW-VE27_yqTEudLcbINc_RwnGYz5bf5x9KgsIorahtvIHKwwoUnPqTNaESpSOwyC0oK5nbTolu9mFvemIs_1NSxxqNYmQx2tF_5g7qRBm256ApZOju7cFRXDCYkuE4pY_tC6zO5iX_7UPUWGBO1Sh0FtwA4_QKkIl7Jnq1BwC30GHXrTgW_Tl8Tu3A",
        "Content-Type": "application/json"}

    vm_data = {
        "id": "/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/myVM",
        "type": "Microsoft.Compute/virtualMachines",
        "properties": {
            "osProfile": {
                "adminUsername": "ry",
                "secrets": [

                ],
                "computerName": "myVM",
                "linuxConfiguration": {
                    "ssh": {
                        "publicKeys": [
                            {
                                "path": "/home/ry/.ssh/authorized_keys",
                                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDEXNfw0c1mn11lDiK+7seMA7eeL21Yc1LFSxwN7/Pfx61VasMsqF8IDct4FcYIq1hOwYA0Px570N0QXBwRnVUWnVwwH7BbsPR75g6WffIV2dEvEyfSA6kPEWTee1I/qzlXGnLq2xM/yb3GyXnkU5VjbPtzJRk3JajD6XE2DiWxgoXra+32tn6TUVnkhNQJOoNzyd3kBbO4nhK8Vyu9qKd907SuhirSfdOHNEkvOlvIEq0n6sEECyRMWeuR8YL8GcNKlv7sW/gNEpJ+/nqf08KeXKeAlTh65OvbkEnXJ9D9lBM1pzEzHZNMP1aQxl08pqUfIRMrREeicvY0ALXKDoMRPiWzyglF5Wik8/IUJ2jJ5mAJEJ1cGoz1XSYmxUKH0zjN9tDrgMU03DhmRaTMeR/6/JDWM6ZfnSpkzVmT9sCRaQJKJabY8zMO6JfjZC/gbkorz2SpNLb7Kur8JTJyzuLy8pZpKe8bD8K3rfFMZNJV/lPN5jZq40/F/0/nCJbfh7c= ry@Rys-MacBook-Pro.local"
                            }
                        ]
                    },
                    "disablePasswordAuthentication": True
                }
            },
            "networkProfile": {
                "networkInterfaces": [
                    {
                        "id": "/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/test-ni",
                        "properties": {
                            "primary": True
                        }
                    }
                ]
            },
            "storageProfile": {
                "imageReference": {
                    "sku": "16.04-LTS",
                    "publisher": "Canonical",
                    "version": "latest",
                    "offer": "UbuntuServer"
                },
                "dataDisks": [

                ]
            },
            "hardwareProfile": {
                "vmSize": "Standard_D1_v2"
            },
            "provisioningState": "Creating"
        },
        "name": "lab4vm",
        "location": "westeurope"
    }

    ni_data = {
        "properties": {
            "ipConfigurations": [
                {
                    "name": "ipconfig1",
                    "properties": {
                        "publicIPAddress": {
                            "id": "/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/test-ip"
                        },
                        "subnet": {
                            "id": "/subscriptions/bc126a7f-1138-4cc6-8a68-5819525a3dd5/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/pis80/subnets/default"
                        }
                    }
                }
            ]
        },
        "location": "westeurope"
    }

    ip_data = {
        "properties": {
            "publicIPAllocationMethod": "Static",
            "idleTimeoutInMinutes": 10,
            "publicIPAddressVersion": "IPv4"
        },
        "sku": {
            "name": "Basic"
        },
        "location": "westeurope"
    }

    response = requests.put(ip_url, headers=headers, json=ip_data)

    print("Status Code", response.status_code)
    print("JSON Response ", response.json())

    response = requests.put(ni_url, headers=headers, json=ni_data)

    print("Status Code", response.status_code)
    print("JSON Response ", response.json())

    response = requests.put(vm_url, headers=headers, json=vm_data)

    print("Status Code", response.status_code)
    print("JSON Response ", response.json())


if __name__ == "__main__":
    main()
