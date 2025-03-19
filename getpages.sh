#!/bin/bash 
for i in {1985..2019} {2021..2024}
do 
    echo "Getting wiki page for ${i}"
    curl -s "https://en.wikipedia.org/w/index.php?title=${i}_NCAA_Division_I_men%27s_basketball_tournament&action=edit" --output "html/${i}.html"
done
