from pathlib import Path
import json

from decouple import config

import word_functions

company_name = config("COMPANY_NAME")

def generate_investor_documents(investors: list[str], documents: list[str]) -> None:
    """Takes a list of investors and documents, and generates a set of documents for each
    investor from the document template."""

    for investor in investors:
        for document in documents:
            generate_document_for_investor(investor, document)

def generate_document_for_investor(investor_name: str, document_name: str) -> None: 
    """Generates a document from the template for the given investor name and document name."""

    # Targets for replacement values
    investor_name_target = "[INVESTOR_NAME]"
    document_name_target = "[DOCUMENT_NAME]"

    template_document_path = Path(r"C:\Users\dunca\Sync\2 - Work\1 - Anuva Investments\1 - Investor Info Portal\1 - Investor Folder Reogranisation\Investor Folder Architecture\2 - Investor Folders for Beta\[TEMPLATE] - Investor Portal Beta Document.docx")


    # Create a dict of find value:replace value
    replacement_mapping = {
        investor_name_target:investor_name,
        document_name_target:document_name
    }

    # Create the filename for this instance of the document
    current_filename = f"(BETA) - {company_name} {document_name} - {investor_name}.docx"

    template_document = word_functions.WordDoc(template_document_path)

    template_document.find_and_replace_in_document(replacement_mapping)
    template_document.save(current_filename, Path("Investors").joinpath(investor_name))




def main():
    """Main function"""

    investor_names = json.loads(config("INVESTOR_NAMES"))
    document_names = json.loads(config("DOCUMENTS_TO_CREATE"))
    generate_investor_documents(investor_names, document_names)


if __name__ == "__main__":
    main()