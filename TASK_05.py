"""
BUSINESS OUTCOME Help a dispatcher accept as many parcels as possible without
overloading a vehicle.
Read a van capacity and a comma-separated sequence of parcel weights. Process weights
from left to right. Accept a parcel when it fits within the remaining capacity. If it does not fit,
reject it and continue checking later parcels. All weights are positive numbers.
Print one decision per parcel, then print the accepted count, loaded weight and remaining
capacity with two decimals.
Example
Van capacity (kg): 100
Parcel weights (kg): 40, 65, 20, 35
Parcel 1: ACCEPTED
Parcel 2: REJECTED
Parcel 3: ACCEPTED
Parcel 4: ACCEPTED
Accepted parcels: 3
Loaded weight: 95.00 kg
Remaining capacity: 5.00 kg
Important interpretation
Rejecting one parcel does not stop the process. A later, lighter parcel may still fit. Your
algorithm therefore needs both accumulated state and a decision inside the loop.
TEST THIS Capacity 50 with weights 50; capacity 50 with weights 51,49; and a sequence
where several rejected parcels appear before one accepted parcel.
"""
def ParcelPacking(vanCap, parcelWeights):
    acceptedParcel = []                                         # Save all accepted parcel
    print(f"Van Capacity (kg): {vanCap}")
    print(f"Parcel Weight (kg): {parcelWeights}")
    
    vanCap = int(vanCap)                                        # Turn inputed van capacity string to integer (May change to float)
    parcelWeights = parcelWeights.replace(" ", "").split(",")   # Turn inputed parcel weight string to list 
    parcelWeights = [int(x) for x in parcelWeights]             # Turn each item in list into integer (May change to float)

    for i in enumerate(parcelWeights):                          # Check if parcel weight fits in van capacity
        if (vanCap - i[1]) >= 0:                                # If so prin "Accepted" and add parcel to list with accepted parcels
            print(f"Parcel {i[0]+1}: Accepted")                 #
            acceptedParcel.append(i[1])                         #
            vanCap = vanCap - i[1]                              #
        else:                                                   # else print "Rejected"
            print(f"Parcel {i[0]+1}: Rejected")                 #

    print(f"Accepted parcels: {len(acceptedParcel)}")           # Results
    print(f"Loaded weight: {sum(acceptedParcel):.2f}kg")        #
    print(f"Remaining Capacity: {vanCap:.2f}kg")                #

if __name__ == "__main__":
    # ParcelPacking("100", "10,70, 40, 20, 500")
    capacity = input("Van capacity (kg): ")
    parcels = input("Parcel weight (kg): ")
    ParcelPacking(capacity, parcels)
