.PHONY: all
all: download-lib download-sources download-javadoc-jars javadocs

.PHONY: download-lib
download-lib:
	mkdir -p opp/lib
	rm -rf opp/lib/*
	mvn dependency:copy-dependencies -DoutputDirectory=opp/lib -Dhttps.protocols=TLSv1.2

.PHONY: download-sources
download-sources:
	mkdir -p opp/sources
	rm -rf opp/sources/*
	mvn dependency:copy-dependencies -Dclassifier=sources -DoutputDirectory=opp/sources \
	  -Dhttps.protocols=TLSv1.2

.PHONY: download-javadoc-jars
download-javadoc-jars:
	mkdir -p opp/javadoc
	rm -rf opp/javadoc/*
	mvn dependency:copy-dependencies -Dclassifier=javadoc -DoutputDirectory=opp/javadoc \
	  -Dhttps.protocols=TLSv1.2

.PHONY: javadocs
javadocs: download-javadoc-jars
	rm -rf javadocs
	mkdir -p javadocs
	python3 ../tools/build-combined-javadoc.py

.PHONY: clean
clean:
	rm -rf javadocs opp/*

.PHONY: dist
dist: javadocs
	rm -rf dist
	mkdir -p dist
	tar czf dist/jump-R2019b-javadocs-0.1.0-SNAPSHOT.tgz javadocs
