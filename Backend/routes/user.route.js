import express from "express";
import { login, register, updateProfile } from "../controllers/user.controller.js";
import isAuthenticated from "../middlewares/isAuthenticated.js";

const router = express.Router();

router.route("/register").post(register); // Registration
router.route("/login").post(login); // Login
router.route("/profile/update").put(isAuthenticated, updateProfile); // Update Profile

export default router;
