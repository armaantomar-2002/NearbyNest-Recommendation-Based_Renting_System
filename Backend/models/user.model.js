import mongoose from "mongoose";

const studentSchema = new mongoose.Schema({
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
        avatar: { type: String , default: ""} 
    },
    locationPreferences: {
        area: { type: String },
        radius: { type: Number } 
    },
    favorites: [
        { type: mongoose.Schema.Types.ObjectId, ref: 'Room' }
    ],
    preferredGender: { type: String, enum: ['Male', 'Female', 'Any'], required: true },
    wifiRequired: { type: Boolean, default: true },
    foodRequired: { type: Boolean, default: false },
    parkingRequired: { type: Boolean, default: false },
    amenitiesRequired: [
        {
            type: String,
            enum: ['Restaurants', 'Gym', 'Grocery Stores', 'Medical Shops', 'Transportation'],
        }
    ],
}, { timestamps: true });

export const User = mongoose.model('User', userSchemna);
