import cv2

def exec_input(input_file_name):
    input_file = cv2.imread(data_path + "/input/" + input_file_name)
    annotation_file = cv2.imread(data_path + "/annotation/" + input_file_name, 0)
    (x_train, y_train) = make_teaching_data(input_file, annotation_file)
    return (input_file, annotation_file)