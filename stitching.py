import os


def stitching_pure_hugin(threshold, max_visible_scale):
    print("stitching button clicked!")
#    os.system("pto_gen *.jpeg -o test.pto")
    #    os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")
    os.system("cpfind --prealigned --kdtreeseconddist=" + str(float(threshold)/100) + " -o control_pts.pto prealigned.pto")
    # pruning control points
        #os.system("cpclean -o control_pts2.pto control_pts.pto")
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    os.system("linefind -o lines.pto pruning_pts.pto")
    # optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    #    os.system("hugin_executor -s optimized.pto -t 10")
    #    os.system("convert *.tif -resize 1500x500 output.jpg")
    #    os.system("rendering/Kirito_rendering 1021700000.jpg 1021700002.jpg 1021700004.jpg 1021700005.jpg 1021700006.jpg 1021700007.jpg 1021700008.jpg 1021700010.jpg 1021700010.jpg 1021700011.jpg 1021700014.jpg 1021700016.jpg 1021700018.jpg 1021700019.jpg 1021700021.jpg 1021700026.jpg 1031700003.jpg 1031700030.jpg 1021700012.jpg")
    #    os.system("rendering/Kirito_rendering mcam_1.jpeg mcam_2.jpeg")
    os.system("pano_modify -o optimized_centered.pto --center --straighten --canvas=AUTO optimzied.pto")
    os.system("python3 update_pto_resolution.py")
    os.system("hugin_executor --stitching optimized_s.pto")
    os.system('convert "1 - 19.tif" preview.jpg')
    # TODO: the json name should be depending on the date
    os.system("python3 HuginMakeSaccadeConfig.py optimized.pto model.json " + max_visible_scale)


def stitching_pure_hugin_without_existing_model(threshold, max_visible_scale):
    print("stitching button clicked!")
    os.system("pto_gen *.jpeg -o init.pto")
    #    os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")
    os.system("cpfind --multirow -o control_pts.pto init.pto")
    # pruning control points
        #os.system("cpclean -o control_pts2.pto control_pts.pto")
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    os.system("linefind -o lines.pto pruning_pts.pto")
    # optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    os.system("pano_modify -o optimized_centered.pto --center --straighten --canvas=AUTO optimized.pto")
    os.system("python3 update_pto_resolution.py")
    os.system("hugin_executor --stitching optimized_s.pto")
    os.system('convert "*.tif" preview.jpg')
    # TODO: the json name should be depending on the date
    os.system("python3 HuginMakeSaccadeConfig.py optimized.pto model.json " + max_visible_scale)


def preview_hugin():
    if not("preview.jpg" in os.listdir()):
        os.system("hugin_executor --stitching optimized.pto")
        os.system('convert "mcam_1 - mcam_19.tif" preview.jpg')
