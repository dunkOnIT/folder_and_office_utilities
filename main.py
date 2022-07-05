from pathlib import Path
import json

from decouple import config

import word_functions

company_name = config("COMPANY_NAME")

def generate_documents_for_investor(investor_name: str) -> None:
    """"""

    # Targets for replacement values
    investor_name_target = "[INVESTOR_NAME]"
    document_name_target = "[DOCUMENT_NAME]"

    # List of documents to generate
    documents_to_generate=json.loads(config("DOCUMENTS_TO_CREATE"))
    template_document_path = Path("[TEMPLATE] - Investor Portal Beta Document.docx")


    # Loop through documents to generate, and create one of each for the investor
    for doc_to_generate in documents_to_generate:

        # Create a dict of find value:replace value
        replacement_mapping = {
            investor_name_target:investor_name,
            document_name_target:doc_to_generate
        }

        # Create the filename for this instance of the document
        current_filename = f"(BETA) - {company_name} {doc_to_generate} - {investor_name}.docx"

        template_document = word_functions.WordDoc(template_document_path)

        template_document.find_and_replace_in_document(replacement_mapping)
        template_document.save(current_filename, Path("Investors").joinpath(investor_name))

def find_and_replace_in_document(find_replace_mapping: dict[str, str]):
    for find_value in find_replace_mapping.keys():
        pass




def main():
    """Main function"""
    generate_documents_for_investor("Duncan Hobbs")


if __name__ == "__main__":
    main()