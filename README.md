# Playwright-Pytest-BDD voor PostNL project
Dit project biedt een voorbeeld voor het testen van een UI met Playwright, geschreven in Python, met behulp van het Page Object Model ontwerppatroon en aangedreven via BDD feature files door middel van Pytest BDD.

## Aan de slag
1. Installeer de [pip](https://pypi.org/project/pip/) package manager;
2. Installeer Python (3.10+);
3. Installeer [JDK](https://corretto.aws/downloads/latest/amazon-corretto-11-x64-macos-jdk.pkg) (vereist voor Allure);
4. Clone de repository;
5. Installeer de projectafhankelijkheden met het volgende commando in de Pycharm terminal: ``` pip install -r requirements.txt ```
6. Installeer Playwright browsers met het volgende commando: ``` playwright install ```

### Tests uitvoeren

- Voer alle tests uit
   ```pytest```
- een specifieke tag uit een feature file uitvoeren
```pytest -k "maak_klant_aan"```

- Voer een specifieke test suite uit
   ```pytest -m <suite_name>```

## Allure rapport genereren
```allure serve allure_results```

_author: Beni Dhomi - QualityAccelerators_