rule all:
    input:
        "data/processed/variants.vcf"

rule copy_vcf:
    input:
        "data/raw/NIST.vcf"
    output:
        "data/processed/variants.vcf"
    shell:
        "cp {input} {output}"
