DNA = input("Please enter the DNA sequence: ").upper()

RNA = DNA.replace("T", "U")

codon_chart = {

    # Phenylalanine
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",

    # Leucine
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",

    # Isoleucine
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",

    # Methionine
    "AUG": "Methionine",

    # Stop codons
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

protein = []

for i in range(0, len(RNA)-2, 3):

    codon = RNA[i:i+3]

    amino_acid = codon_chart.get(codon, "Unknown")

    if amino_acid == "STOP":
        break

    protein.append(amino_acid)

print("Protein sequence:")
print("-".join(protein))
