all: settings.py people.json EMAIL_MESSAGE

clean:
	@rm settings.py people.json EMAIL_MESSAGE

settings.py:
	@test -f $@ || cp example_$@ $@

people.json:
	@test -f $@ || cp example_$@ $@

EMAIL_MESSAGE:
	@test -f $@ || cp example_$@ $@

.PHONY: all clean
