from dataPrep import load_and_clean_data
from DataSet import prepare_dataset


def main():
    # Load and clean data
    filepath = r'..\Modern-Software-Project\dataFiles\Meditations.txt'
    cleaned_text = load_and_clean_data(filepath)

    # Prepare dataset
    input_ids, attention_masks = prepare_dataset([cleaned_text])

    # Here you can add more logic, e.g., to train a model or generate text

    print("Dataset prepared with input IDs:", input_ids)
    print("Attention masks:", attention_masks)


if __name__ == "__main__":
    main()
