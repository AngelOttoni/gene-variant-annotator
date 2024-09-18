from flask import Flask, request, jsonify, render_template
import pysam
import pandas as pd

app = Flask(__name__)

# Function to load and filter data
def load_and_filter_vcf(min_freq, min_dp):
    # Upload the VCF file
    vcf_file = 'results/annotated_variants.vcf'
    vcf = pysam.VariantFile(vcf_file)
    
    # Create a list to store variants
    variants = []
    
    # Iterate over variants in VCF file
    for rec in vcf.fetch():
        freq = rec.info.get('AF', [0])[0]  # Example of how to get the frequency (AF)
        dp = rec.info.get('DP', 0)          # Depth (DP)
        
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