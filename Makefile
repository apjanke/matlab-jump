.PHONY: internal-jar-poms
internal-jar-poms:
	python3 tools/create_internal_jars_pom.py R2016b
	python3 tools/create_internal_jars_pom.py R2019b
	python3 tools/create_internal_jars_pom.py R2020a