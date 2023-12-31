import Router  from "express-promise-router";
import { profile, signin, signout, signup } from "../controllers/auth.controller.js";
import { isAuth } from "../middleware/auth.middleware.js";

const router = Router();

router.post("/signin", signin);
router.post("/signup", signup);
router.post("/signout", signout);
router.get("/profile",isAuth, profile);

export default router;