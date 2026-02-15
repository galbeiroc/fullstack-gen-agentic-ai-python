chai_type = "Ginger chai"
customer_name = "Almendra"

print(f"Order for {customer_name} : {chai_type} please!")

print(f"{customer_name[0]}") # A

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}") # First word: Aromatic
print(f"Last word: {chai_description[12:]}") # Last word Bold
print(f"Jump word: {chai_description[0:8:3]}") # jump each character 3 'Ami'

print(f"Reverse string {chai_description[::-1]}") # Reverse string dloB dna citamorA

label_text = "Spécial Character"
enconded_text = label_text.encode("utf-8")
print(f"None Encoded text: {label_text}") # Spécial Character
print(f"Encoded text: {enconded_text}") # b'Sp\xc3\xa9cial Character'
print(f"Decoded text: {enconded_text.decode('utf-8')}") # Spécial Character