class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 1) {
            return false;
        }

        List<Integer> listCount = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (listCount.contains(nums[i])) {
                return true;
            }
            listCount.add(nums[i]);
        }
        return false;
    }
}