# Market Map - click progress fixed

Upload these files together to GitHub Pages:

- index.html
- settlements_flat.json
- settlements_wkt_2039.json

The click selection now uses GovMap displayGeometries().progress(...) for drawn polygons, plus GovMap getLayerData and local point-in-polygon as fallbacks.
