# from abc import ABC
# from unittest import TestCase
# from unittest import mock
# from unittest.mock import MagicMock


# class Sensor:
#     class Observer(ABC):
#         def movement_was_detected(self):
#             raise NotImplementedError()

#         def movement_was_stopped(self):
#             raise NotImplementedError()

#     detecting_movement = False
#     observer = None

#     def detect_movement(self):
#         self.detecting_movement = True
#         if self.observer is not None:
#             self.observer.movement_was_detected()

#     def stop_detect_movement(self):
#         self.detecting_movement = False
#         if self.observer is not None:
#             self.observer.movement_was_stopped()

#     def register(self, observer: Observer):
#         self.observer = observer


# class VideoRecorder:
#     is_recording = False

#     def start_recording(self):
#         self.is_recording = True

#     def stop_recording(self):
#         self.is_recording = False


# class System(Sensor.Observer):
#     def __init__(self, sensor: Sensor, camera: VideoRecorder) -> None:
#         self.camera = camera
#         sensor.register(self)

#     def movement_was_detected(self):
#         self.camera.start_recording()

#     def movement_was_stopped(self):
#         self.camera.stop_recording()


# class TestVideoRecorder(TestCase):
#     def test_not_recording_after_creation(self):
#         video_recorder = VideoRecorder()
#         assert not video_recorder.is_recording

#     def test_start_recording(self):
#         video_recorder = VideoRecorder()
#         video_recorder.start_recording()
#         assert video_recorder.is_recording

#     def test_multiple_video_recorders_start_recording(self):
#         video_recorder1 = VideoRecorder()
#         video_recorder2 = VideoRecorder()
#         video_recorder1.start_recording()
#         assert video_recorder1.is_recording
#         assert not video_recorder2.is_recording

#     def test_stop_recording(self):
#         video_recorder = VideoRecorder()
#         video_recorder.stop_recording()
#         assert not video_recorder.is_recording

#     def test_start_and_then_stop_recording(self):
#         video_recorder = VideoRecorder()
#         video_recorder.start_recording()
#         video_recorder.stop_recording()
#         assert not video_recorder.is_recording


# class TestSensor(TestCase):
#     def test_not_detecting_movement(self):
#         sensor = Sensor()
#         assert not sensor.detecting_movement

#     def test_detecting_movement(self):
#         sensor = Sensor()
#         sensor.detect_movement()
#         assert sensor.detecting_movement

#     def test_stop_detecting_movement(self):
#         sensor = Sensor()
#         sensor.detect_movement()
#         sensor.stop_detect_movement()
#         assert not sensor.detecting_movement

#     def test_send_signal_when_detecting_movement(self):
#         sensor = Sensor()
#         observer = mock.create_autospec(spec=Sensor.Observer)
#         sensor.register(observer)
#         sensor.detect_movement()
#         observer.movement_was_detected.assert_called_once()

#     def test_stop_signal_when_stop_detecting_movement(self):
#         sensor = Sensor()
#         observer = MagicMock()
#         sensor.register(observer)
#         sensor.detect_movement()
#         sensor.stop_detect_movement()
#         observer.movement_was_stopped.assert_called_once()


# class TestSystem(TestCase):
#     def test_not_detecting_movement(self):
#         sensor = Sensor()
#         camera = VideoRecorder()
#         system = System(sensor, camera)
#         assert not camera.is_recording

#     def test_start_recording_when_detecting_movement(self):
#         sensor = Sensor()
#         camera = VideoRecorder()
#         system = System(sensor, camera)
#         sensor.detect_movement()
#         assert camera.is_recording

#     def test_stop_recording_when_stop_detecting_movement(self):
#         sensor = Sensor()
#         camera = VideoRecorder()
#         system = System(sensor, camera)
#         sensor.detect_movement()
#         sensor.stop_detect_movement()
#         assert not camera.is_recording
