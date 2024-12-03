import mongoose from "mongoose";

const roomOwnerSchema = new mongoose.Schema({
    fullname: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    phoneNumber: {
        type: Number,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    profile: {
        bio: { type: String },
        avatar: { type: String, default: "" }
    },
    address: {
        city: { type: String, required: true },
        state: { type: String, required: true },
        zipCode: { type: String, required: true }
    },
    roomListings: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Room'
        }
    ],
    amenitiesProvided: [
        {
            type: String,
            enum: ['WiFi', 'Food', 'Parking', 'Restaurants', 'Gym', 'Grocery Stores', 'Medical Shops', 'Transportation'],
        }
    ],
    termsAccepted: { type: Boolean, required: true, default: false }
}, { timestamps: true });

export const RoomOwner = mongoose.model('RoomOwner', roomOwnerSchema);
