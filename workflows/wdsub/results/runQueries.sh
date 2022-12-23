#!/bin/bash

EndpointURL=http://156.35.94.157/data/query

helpFunction()
{
   echo ""
   echo "Usage: $0 -v <versionNumber> -y <year>"
   echo -e "\t-v version number, something like '0.0.3'"
   echo -e "\t-y year, something like '2017'"
   exit 1 # Exit script after printing help
}

while getopts "v:y:" option ;
do
   case "${option}" in
      v ) 
      version="${OPTARG}" ;;
      y ) 
      year="${OPTARG}" ;;
      ? ) 
      helpFunction ;; 
   esac
done

if [ -z "${version}" ]
then
   echo "Version is empty";
   helpFunction
fi

if [ -z "$year" ] 
then
   echo "Year is empty";
   helpFunction
fi

docker run -d -v /home/labra/SubShEx2SPARQL/shex:/shex \
           -v /home/labra/biohackathon2022/workflows/wdsub/results:/results \
           wesogroup/subshex2sparql:${version} \
           --shex /shex/GeneWiki.shex \
           --runQueries \
           --endpoint ${EndpointURL} \
           --outputFormat CSV \
           --outputResults /results/GeneWiki${year}.csv
              