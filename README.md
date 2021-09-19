# ta-hackaton-2021-emerald
Test Automation Hackaton 2021. Emerald team's repo.


1. Запуск автотестов

Запуск автотестов происходит из командной строки с помощью команды "python runner.py {threads} {results_dir_name} {optional: add_command_line_options}"

threads - Количество потоков, integer

results_dir_name - Название директории, куда будут складываться json файлы с рез-тами теста. string

add_command_line_options: - дополнительные параметры командной строки, которые будут переданы в pytest
Например '--test-group=product' или '--k test_product.py --test-group=product'


add_command_line_options ДОЛЖНЫ БЫТЬ В КАВЫЧКАХ


--test-group - Название метки, по которой будет выбрана группа тестов для запуска. store_openings

--log-level - Уровень логирования (DEBUG, INFO...). логи пишутся в папку logs

Пример запуска теста в 3 потока для всех тестов с меткой product: python .\runner.py 3 results '--test-group=product'
(Tc)


После прохождения автотестов в директорию {results_dir_name} будут добавлены json и xml файлы с результами выполнения тестов pytest
