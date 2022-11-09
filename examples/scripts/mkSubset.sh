#!/bin/sh
Version=0.0.29
Dump2018=wikidata-20180115-all
Dump2022=wikidata-20220630-all
Lines=3000lines

ShExName=GeneWiki
DumpFile=${Lines}
SchemaFormat=ShExC
DumpMode=OnlyMatched
DumpFormat=JSON
docker run -d -v /home/labra/dumps:/data -v /home/labra/wdsubConfig/shex:/shex -v /home/labra/generatedDumps:/generatedDumps wesogroup/wdsub:${Version} dump -o /generatedDumps/${ShExName}_${DumpFile}.json.gz -s /shex/${ShExName}.shex /data/${DumpFile}.json.gz --dumpFormat ${DumpFormat} --dumpMode ${DumpMode} --schemaFormat ${SchemaFormat}