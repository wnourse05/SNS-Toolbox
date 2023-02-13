echo 'Starting Test for Intel NUC'
echo ''
echo 'Nonspiking Dense:'
python3 test_backend_speed_nonspiking_dense.py
echo ''
echo 'Nonspiking Sparse:'
python3 test_backend_speed_nonspiking_sparse.py
echo ''
echo 'Spiking Dense:'
python3 test_backend_speed_spiking_dense.py
echo ''
echo 'Spiking Sparse:'
python3 test_backend_speed_spiking_sparse.py
echo ''
echo 'Testing finished, all data recorded'