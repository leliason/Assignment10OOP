from Persistence.api_client import ApiClient
from Persistence.repository import Repository
from Services.Cleaner import Cleaner
from Services.analyzer import Analyzer
from UI.cli import CLI

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