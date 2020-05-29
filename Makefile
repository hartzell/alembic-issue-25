.PHONY: setup
setup:
	mkdir deps
	poetry install

.PHONY: test
test:
	PGURI=postgresql://postgres:example@localhost/issue_25_$$$$ pytest -v -s tests/issue-25.py

.PHONY: clean
clean:
	rm -rf \
	alembic/__pycache__ \
	alembic/versions/__pycache__ \
	tests/__pycache__

.PHONY: veryclean
veryclean: clean
	rm -rf deps
