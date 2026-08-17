"Convert DNA to RNA"
DNA_RNA = {
    "G":"C",
    "C":"G",
    "T":"A",
    "A":"U"
}
def to_rna(dna_strand):
    "Convert to RNA"
    result = ""
    for dna in dna_strand:
        result+=DNA_RNA[dna]
    return result
