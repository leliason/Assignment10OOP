from persistence.api_client import ApiClient
from persistence.repository import Repository
from services.cleaner import Cleaner
from services.analyzer import Analyzer
from ui.cli import CLI

def main():
    api_client = ApiClient()
    repository = Repository()
    cleaner = Cleaner()
    analyzer = Analyzer()

    app = CLI(
        api_client=api_client,
        repository=repository,
        cleaner=cleaner,
        analyzer=analyzer
    )
    app.run()

if __name__ == "__main__":
    main()