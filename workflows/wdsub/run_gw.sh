# -----------------------------------------------------------------------
# CONFIGURATION VARIABLES
shex_files_path='/home/andra/projects/biohackathon2022/workflows/wdsub';
shex_file_names=(gene);
results_files_path='/home/andra/projects/biohackathon2022/workflows/wdsub/results';
data_files_path='/home/andra/projects/biohackathon2022/workflows/wdsub/data';
# -----------------------------------------------------------------------
# DO NOT MODIFY ANYTHING BELOW THIS LINE!!!

echo 'Welcome to WDSub GenWiki!';
echo 'This script will create a subset for each defined shape.';

echo 'Pulling wdsub docker image...';
docker pull wesogroup/wdsub:0.0.29;



for shex_file_name in "${shex_file_names[@]}"
do
    echo "Creating subset for ${shex_files_path}/${shex_file_name}.shex";
    dockerID=`docker run -d -v $data_files_path:/data \
        -v $shex_files_path:/shex \
        -v $results_files_path:/dumps \
        wesogroup/wdsub:0.0.27 dump \
        -o /dumps/result_$shex_file_name.json.gz \
        -s /shex/$shex_file_name.shex \
        --processor WDTK \
        --dumpFormat Turtle \
        --dumpMode WholeEntity \
        --schemaFormat ShExC \
        /data/wikidata-20220103-all.json.gz;`
    echo "Subsetting is being created  for ${shex_files_path}/${shex_file_name}.shex";
    echo "Check ${dockerID} for progres" 
done
