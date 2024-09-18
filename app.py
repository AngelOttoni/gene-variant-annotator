from flask import Flask, request, jsonify, render_template
import pysam
import pandas as pd

app = Flask(__name__)

# Função para carregar e filtrar dados
def load_and_filter_vcf(min_freq, min_dp):
    # Carregar o arquivo VCF
    vcf_file = 'results/annotated_variants.vcf'
    vcf = pysam.VariantFile(vcf_file)
    
    # Criar uma lista para armazenar variantes
    variants = []
    
    # Iterar sobre variantes no arquivo VCF
    for rec in vcf.fetch():
        freq = rec.info.get('AF', [0])[0]  # Exemplo de como pegar a frequência (AF)
        dp = rec.info.get('DP', 0)          # Profundidade (DP)
        
        if freq >= min_freq and dp >= min_dp:
            variants.append({
                'chrom': rec.chrom,
                'pos': rec.pos,
                'id': rec.id,
                'ref': rec.ref,
                'alt': ','.join(rec.alts),
                'frequency': freq,
                'DP': dp
            })
    
    return variants

@app.route('/filter', methods=['GET'])
def filter_variants():
    min_freq = float(request.args.get('min_freq', 0))
    min_dp = int(request.args.get('min_dp', 0))
    filtered_data = load_and_filter_vcf(min_freq, min_dp)
    return jsonify(filtered_data)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)