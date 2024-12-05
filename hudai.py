# import mne
#
# # Path to an .edf file (replace with your file path)
# file_path = "chb01_01.edf"
#
# # Load the EEG data
# raw_data = mne.io.read_raw_edf(file_path, preload=True)
#
# # Plot EEG signals
# raw_data.plot(title="EEG Data Visualization", duration=10, start=0)  # duration: seconds to show per window

#           ///////////////////


# import mne
# import matplotlib.pyplot as plt
#
# # Path to the .edf file
# file_path = "chb01_01.edf"
#
# # Load the EEG data
# raw_data = mne.io.read_raw_edf(file_path, preload=True)
#
# # Check available channel names
# print("Available channels:", raw_data.info['ch_names'])
#
# # Pick valid channels from the dataset
# channels = ['FP1-F7', 'F7-T7', 'T7-P7']  # Example: Select 3 channels for clarity
# raw_data.pick(channels)  # Select these channels
#
# # Extract data and times
# data, times = raw_data.get_data(return_times=True)
#
# # Create a better plot for the selected channels
# plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
# for i, channel in enumerate(channels):
#     plt.plot(times, data[i] + i * 100, label=channel)  # Offset signals for clarity
#
# # Add labels, title, and legend
# plt.title("EEG Visualization for Selected Channels", fontsize=16)
# plt.xlabel("Time (s)", fontsize=14)
# plt.ylabel("Amplitude (µV)", fontsize=14)
# plt.legend(loc='upper right', fontsize=12)
# plt.grid(True)
# plt.tight_layout()
# plt.show()



#   /////////////////////
#
# import mne
# import matplotlib.pyplot as plt
#
# # Path to the .edf file
# file_path = "chb01_01.edf"
#
# # Load the EEG data
# raw_data = mne.io.read_raw_edf(file_path, preload=True)
#
# # Print available channels
# print("Available channels:", raw_data.info['ch_names'])
#
# # Pick valid channels from the dataset
# channels = ['FP1-F7', 'F7-T7', 'T7-P7']  # Replace with your channels of interest
# raw_data.pick(channels)  # Select these channels
#
# # Apply scaling to data if necessary
# raw_data.apply_function(lambda x: x * 1e6)  # Convert to microvolts (µV)
#
# # Extract data and times
# data, times = raw_data.get_data(return_times=True)
#
# # Verify data sample
# print("Sample data:", data[:, :100])
#
# # Create a better plot for the selected channels
# plt.figure(figsize=(12, 6))
# for i, channel in enumerate(channels):
#     plt.plot(times, data[i] + i * 100, label=channel)  # Adjust scaling as needed
#
# # Add labels, title, and legend
# plt.title("EEG Visualization for Selected Channels", fontsize=16)
# plt.xlabel("Time (s)", fontsize=14)
# plt.ylabel("Amplitude (µV)", fontsize=14)
# plt.legend(loc='upper right', fontsize=12)
# plt.grid(True)
# plt.tight_layout()
# plt.show()


#           //////////////////////////



import mne
import matplotlib.pyplot as plt

# Path to the .edf file
file_path = "chb01_01.edf"

# Load the EEG data
raw_data = mne.io.read_raw_edf(file_path, preload=True)

# Print available channels
print("Available channels:", raw_data.info['ch_names'])

# Pick valid channels from the dataset
channels = ['FP1-F7', 'F7-T7', 'T7-P7']  # Replace with your channels of interest
raw_data.pick(channels)  # Select these channels

# Apply scaling to data if necessary
raw_data.apply_function(lambda x: x * 1e6)  # Convert to microvolts (µV)

# Extract data and times
data, times = raw_data.get_data(return_times=True)

# Verify data sample
print("Sample data:", data[:, :100])

# Create a better plot for the selected channels
plt.figure(figsize=(12, 6))
colors = ['blue', 'orange', 'green']  # Colors for the channels
for i, (channel, color) in enumerate(zip(channels, colors)):
    plt.plot(times, data[i] + i * 200, label=channel, color=color)  # Offset with color

# Highlight specific events (optional)
event_times = [1000, 2000]  # Example event times in seconds
for event in event_times:
    plt.axvline(event, color='red', linestyle='--', label=f"Event at {event}s")

# Add zoomed x-axis window (optional)
plt.xlim(0, 10)  # First 10 seconds of data

# Add labels, title, and legend
plt.title("EEG Visualization for Selected Channels", fontsize=16)
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Amplitude (µV)", fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True)

# Save the plot (optional)
plt.savefig('eeg_plot.png', dpi=300)

# Show the plot
plt.tight_layout()
plt.show()


