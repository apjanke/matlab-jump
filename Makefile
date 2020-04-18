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

.PHONY: download-javadoc
download-javadoc:
	mkdir -p opp/javadoc
	rm -rf opp/javadoc/*
	mvn dependency:copy-dependencies -Dclassifier=javadoc -DoutputDirectory=opp/javadoc \
	  -Dhttps.protocols=TLSv1.2

.PHONY: combined-javadoc
combined-javadoc:
	python3 build-combined-javadoc.py
