rm -rf build dist src/*.egg-info
rm -rf src/pyearth/{_util.c,_basis.c,_types.c,_knot_search.c,_forward.c,_pruning.c,_qr.c,_record.c}
rm -rf src/pyearth/*.so
find . -name __pycache__ -exec rm -r {} +
