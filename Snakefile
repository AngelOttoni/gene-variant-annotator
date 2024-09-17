shell.prefix("source /home/angel-ottoni/miniforge3/bin/activate /home/angel-ottoni/Documents/computer-science/gene-variant-annotator0/.snakemake/conda/885258ee ")

# Meta-rule that defines the final pipeline files
rule all:
    input:
        # 'data/processed/variants.vcf'
        'results/annotated_variants.vcf'

# Commenting out the copy_vcf rule as it was already executed
# rule copy_vcf:
#     input:
#         'data/raw/NIST.vcf'
#     output:
#         'data/processed/variants.vcf'
#     conda:
#         'envs_conda/snakemake_env.yaml'
#     shell:
#         'cp {input} {output}'

# Rule for variant annotation
rule annotate_variants:
    input:
        vcf='data/processed/variants.vcf'
    output:
        annotated_vcf='results/annotated_variants.vcf'
    log:
        'logs/snpEff_annotation.log'
    conda:
        'envs_conda/snakemake_env.yaml'
    shell:
        'java -jar /home/angel-ottoni/miniforge3/envs/snakemake_env/share/snpeff-5.2-1/snpEff.jar ann -v GRCh38.86 {input.vcf} > {output.annotated_vcf} 2> {log}'