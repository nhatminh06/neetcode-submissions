class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        for (int i = 0; i < nums.length; i ++) {
            for (int j = 1; j < nums.length && i != j; j ++) {
                if (nums[i] + nums[j] == target) {
                    if (i < j) {
                        ans[0] = i;
                        ans[1] = j;
                    }
                    else {
                        ans[0] = j;
                        ans[1] = i;
                    }
                    break;
                }
            }
        }
        return ans;
    }
}
