# @BEGIN collect_data_set
# @PARAM cassette_id  @PARAM accepted_sample @PARAM num_images @PARAM energies
# @OUT sample_id @OUT energy @OUT frame_number
# @OUT raw_image_path @AS raw_image 
# ... @URI file:run/raw/{cassette_id}/{sample_id}/e{energy}/image_{frame_number}.raw            
run_log.write("Collecting data set for sample {0}".format(accepted_sample))
sample_id = accepted_sample
for energy, frame_number, intensity, raw_image_path in collect_next_image(
                           cassette_id, sample_id, num_images, energies, 
                           "run/raw/{cassette_id}/{sample_id}/e{energy}/image_{frame_number:03d}.raw"):
    run_log.write("Collecting image {0}".format(raw_image_path))                
# @END collect_data_set 

# @BEGIN transform_images
# @PARAM sample_id @PARAM energy @PARAM frame_number
# @IN raw_image_path @AS raw_image
# @IN calibration_image @URI file:calibration.img
# @OUT corrected_image @URI file:run/data/{sample_id}/{sample_id}_{energy}eV_{frame_number}.img
# @OUT corrected_image_path @OUT total_intensity @OUT pixel_count
    corrected_image_path = "run/data/{0}/{0}_{1}eV_{2:03d}.img".format(sample_id, energy, frame_number)
    (total_intensity, pixel_count) = transform_image(raw_image_path, corrected_image_path, "calibration.img")
    run_log.write("Wrote transformed image {0}".format(corrected_image_path))
# @END transform_images

