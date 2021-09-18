# ta-hackaton-2021-emerald
Test Automation Hackaton 2021. Emerald team's repo.


1. Запуск автотестов

Запуск автотестов происходит из командной строки с помощью команды "python runner.py {threads} {results_dir_name} {optional: add_command_line_options}"

threads - Количество потоков, integer

results_dir_name - Название директории, куда будут складываться json файлы с рез-тами теста. string

add_command_line_options: - дополнительные параметры командной строки, которые будут переданы в pytest
Например '--test-group=product' или '--k test_product.py'


--test-group - Название метки, по которой будет выбрана группа тестов для запуска. store_openings

Пример запуска теста в 3 потока для всех тестов с меткой product: python .\runner.py 3 'results' '--test-group=product' 
