#!/bin/bash
clear
echo ""

echo "PQ1:  What program blocks are immediately downstream of calculate_strategy?"
dlv -silent -pfilter=pq1 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ2:  What program blocks are anywhere downstream of calculate_strategy?"
dlv -silent -pfilter=pq2 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ3:  What program blocks are immediately upstream of transform_image?"
dlv -silent -pfilter=pq3 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ4:  What program blocks are anywhere upstream of transform_image?"
dlv -silent -pfilter=pq4 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ5:  What channels are immediately downstream of raw_image?"
dlv -silent -pfilter=pq5 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ6:  What channels are downstream of accepted_sample?"
dlv -silent -pfilter=pq6 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ7:  What channels are immediately upstream of corrected_image?"
dlv -silent -pfilter=pq7 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ8: What channels are upstream of raw_image?"
dlv -silent -pfilter=pq8 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ9: What URI variables are associated with data written to the corrected_images channel?"
dlv -silent -pfilter=pq9 example-data.dlv queries-w-prospective.dlv

echo ""
echo "PQ10: What URI variables do channels raw_image and corrected_image have in common?"
dlv -silent -pfilter=pq10 example-data.dlv queries-w-prospective.dlv


echo ""

echo ""
echo "Q1 output:"
dlv -silent -pfilter=q1 example-data.dlv queries-w-prospective.dlv

echo ""
echo "Q2 output:"
dlv -silent -pfilter=q2 example-data.dlv queries-w-prospective.dlv

echo ""
echo "Q3A: What Uri variable values are associated with resource ./run/data/DRT322/DRT322_11000eV_028.img?"
dlv -silent -pfilter=q3a example-data.dlv queries-w-prospective.dlv

echo ""
echo "Q3B: Where is the raw image from which corrected image ./run/data/DRT322/DRT322_11000eV_028.img is derived?"
dlv -silent -pfilter=q3b example-data.dlv queries-w-prospective.dlv

echo ""
echo "Q4 output:"
dlv -silent -pfilter=q4 example-data.dlv queries-w-prospective.dlv

echo ""
echo "Q5: Where is the spreadsheet that led to the corrected image ./run/data/DRT240/DRT240_10000eV_010.img?"
dlv -silent -pfilter=q5 example-data.dlv queries-w-prospective.dlv

echo ""



