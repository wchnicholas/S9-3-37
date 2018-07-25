for resi in 38 50
do
for i in {1..18}
do
echo "working on H$i"
grep H$i\N result/Resi$resi\.tsv | cut -f3 > tmp/resi$resi\.tmp.fa
/Users/wchnicholas/Bioinformatics/weblogo-3.6.0/weblogo -A protein -f tmp/resi$resi\.tmp.fa -U probability --resolution 600 --show-yaxis NO --show-xaxis NO -F png -s large --aspect-ratio 3 -o graph/Resi$resi\_H$i\.png
rm tmp/resi$resi\.tmp.fa
done
done
