ifeq ($(OS), Windows_NT)
main.py: main.py
	python main.py
file_querry.py: file_querry.py
	python file_querry.py
run: main.py file_querry.py
install: 
	copy %cd%/main.py  C:\Users\%username%\Start
	copy %cd%/file_querry.py  C:\Users\%username%\Start
	copy %cd%/funcs_for_file_querry.py  C:\Users\%username%\Start
setup: library.txt
	pip install -r library.txt
install:
	xcopy <название папки с файлами> <директория>
clean:
	del C:\Users\%username%\Start
	del info.txt


else:
main.py: main.py
	python main.py
file_querry.py: file_querry.py
	python file_querry.py
run: main.py file_querry.py
install:
	sudo ln -s "$path/main.py" "/home/$USER/Рабочий стол/Start"
	sudo ln -s "$path/file_querry.py" "/home/$USER/Рабочий стол/Start"
	sudo ln -s "$path/funcs_for_file_querry.py" "/home/$USER/Рабочий стол/Start"

setup: library.txt
	pip install -r library.txt
clean:
	sudo rm "/home/$USER/Рабочий стол/Start"
	sudo rm info.txt
endif
