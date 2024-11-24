import axios from "axios"
import { BEST_PERFOMANCE, COWS, EVALUATE } from "./constants"

export const evaluateGenetics = async () => {
  return axios.get(EVALUATE)
}

export const getBestPerfomance = async () => {
  return axios.get(BEST_PERFOMANCE)
}

export const getCows = async () => {
  return axios.get(COWS)
}

export const getMatch = async (cowId) => {
  return axios.get(`${MATCH}${cowId}`)
}