convert_notebook() {
    local format=$1
    local notebook="/Users/mac/Desktop/CryptAnalysis/presentation/Group_6_Project_Assignment.ipynb"
    
    if [[ "$format" == "web" ]]; then
        jupyter nbconvert "$notebook" --to slides --post serve
    elif [[ "$format" == "pdf" ]]; then
        jupyter nbconvert "$notebook" --to webpdf 
    else
        echo "Invalid format. Use 'web' for HTML or 'pdf' for WebPDF."
    fi
}

convert_notebook "$1"  # Call function with first script argument
