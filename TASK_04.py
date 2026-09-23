#Task_04: Consolidate parcel labels
#BUSINESS OUTCOME Turn duplicate scan data into a clean loading list without losing operational order.
#CLIENT EXPECTATION The printed order matters because warehouse staff load parcels in the order shown by the console.

def ConsolidateParcelLabels(scanned_labels):
    labels = scanned_labels.split(",")
    unique_labels =[]
    #User Input could be: gb-104, GB-220, gb-104, se-011, GB-220
    print(f"Scanned labels: {scanned_labels}")

    for label in labels:
        label = label.strip().upper()

        if label not in unique_labels:
            unique_labels.append(label)

    print("Unique load list:")
    #Create a loop for printing all unique labels.
    for i in range(len(unique_labels)):
        print(f"{i + 1}. {unique_labels[i]}")
    print(f"Total unique parcels: {len(unique_labels)}")

if __name__ == "__main__":
    scanned_labels = (input("Scanned labels:"))