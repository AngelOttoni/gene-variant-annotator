# **Gene Variant Annotator Pipeline**

- This project provides a workflow for annotating gene variants using the [`SnpEff`](http://pcingola.github.io/SnpEff/) tool. The results are presented through a Flask web application, which allows filtering of variants by frequency and depth of coverage (DP).

## **Project Structure**

```
data/
    processed/
        variants.vcf
    raw/
        NIST.vcf
envs_conda/
logs/
    snpEff_annotation.log
results/
    reports/
        snpEff_genes.txt
        snpEff_summary.html
    annotated_variants.vcf
templates/
    index.html
app.py
Dockerfile
LICENSE
README.md
requirements.txt
Snakefile
.gitignore
```

## **Prerequisites**

- [Docker](https://docs.docker.com/get-docker/)
- [Conda or Mamba](https://docs.conda.io/en/latest/miniconda.html)
- [Python 3.6+](https://www.python.org/downloads/)
  
## **Setup and Usage**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/gene-variant-annotator.git
cd gene-variant-annotator
```

### **2. Set Up Conda Environment**

If you prefer to use Conda:

```bash
mamba env create -f envs_conda/snakemake_env.yaml
conda activate snakemake_env
```

### **3. Run the Snakemake Pipeline**

To annotate the variants:

```bash
snakemake --use-conda
```

This will generate the following output files:
- `results/annotated_variants.vcf`: Annotated variants file
- `logs/snpEff_annotation.log`: Log file for the annotation step
- `results/reports/`: Detailed reports (`snpEff_genes.txt`, `snpEff_summary.html`)

### **4. Run the Flask Web Application**

To filter variants by frequency and DP, run the Flask app:

```bash
flask app.py
```

Open `http://localhost:5000` in your browser.

### **5. Using Docker**

Alternatively, you can run the project in a Docker container.

#### **Build the Docker image**

```bash
docker build -t gene-variant-annotator .
```

#### **Run the container**

```bash
docker run -p 5000:5000 gene-variant-annotator
```

This will start the Flask web application inside the Docker container.

## **API Usage**

Once the Flask app is running, the API can be accessed at:

```
GET /api/variants
```

Query parameters:
- `frequency`: Filter variants by allele frequency
- `depth`: Filter variants by depth of coverage (DP)

## **Project Outputs**

The results are located in the `results/` directory:
- `annotated_variants.vcf`: Final output with annotated variants
- `snpEff_genes.txt`: Detailed gene report
- `snpEff_summary.html`: HTML summary of variant annotation

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
